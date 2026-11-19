from ptcgo.game.card_effects.attacks_common import place_counters
from ptcgo.game.card_effects.passives_common import on_ko_from_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, Triggers, unimplemented
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities, SpecialConditions


async def _confuse_if_damaged(ctx):
    attacker = ctx.attacker
    if attacker is not None and attacker.get_attribute(AttrID.HP, 0) < ctx.max_hp(attacker):
        await ctx.apply_special_condition(ctx.defender, SpecialConditions.CONFUSED)


async def _resent(ctx):
    attacker = ctx.ko_attacker
    if attacker is None:
        return
    name = attacker.get_attribute(AttrID.EVOLUTION_LOGIC_NAME)
    for pokemon in ctx.opponent_pokemon_in_play():
        if pokemon.get_attribute(AttrID.EVOLUTION_LOGIC_NAME) == name:
            await ctx.deal_damage(40, target=pokemon, as_counters=True)

card = PokemonCardDef(
    guid="565cd8ae-2bf3-5e1a-b184-3127b3b3fe3d",
    key="DP6",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shedinja.Name",
    display_name="Shedinja",
    searchable_by=["Shedinja", "Stage 1", "Shedinja"],
    subtypes=["Stage 1"],
    collector_number=40,
    set_code="DP6",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Nincada.Name",
    family_id=290,
    abilities=[
        Ability(
            title="Resent",
            game_text="Once during your opponent's turn, if Shedinja would be Knocked Out by damage from an attack, you may put 4 damage counters on the Attacking Pok\u00e9mon and each of the opponent's Pok\u00e9mon that has the same name as the Attacking Pok\u00e9mon.",
            trigger=Triggers.ON_KNOCKED_OUT,
            effect=on_ko_from_attack(_resent),
        ),
        Attack(
            title="Curse and Deceive",
            game_text="Put 3 damage counters on the Defending Pok\u00e9mon. If Shedinja has any damage counters on it, the Defending Pok\u00e9mon is now Confused.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=place_counters(3, target="opponent_active",
                                  also=_confuse_if_damaged),
        ),
    ],
)