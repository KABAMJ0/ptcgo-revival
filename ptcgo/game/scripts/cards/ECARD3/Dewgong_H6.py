from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.attacks_common import count_retreat_cost, damage_per


async def _freeze_lock(ctx):
    await ctx.deal_damage()
    results = await ctx.flip_coins(1, "Freeze Lock")
    if not (results and results[0]):
        return
    active = ctx.opponent_active()
    if active is not None:
        ctx.restrict_attachments(active, ctx.session.turn_state.turn_number + 2)


card = PokemonCardDef(
    guid="4ba68a30-2326-59ac-a144-ac713c85afeb",
    key="ECARD3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Dewgong.Name",
    display_name="Dewgong",
    searchable_by=["Dewgong", "Stage 1", "Dewgong"],
    subtypes=["Stage 1"],
    collector_number=6,
    set_code="ECARD3",
    rarity=Rarities.RareHolo,
    hp=80,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Seel.Name",
    family_id=86,
    abilities=[
        Attack(
            title="Freeze Lock",
            game_text="Flip a coin. If heads, your opponent can't attach Energy cards from his or her hand to his or her Active Pok\u00e9mon during his or her next turn.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=_freeze_lock,
        ),
        Attack(
            title="Crushing Ice",
            game_text="This attack does 40 damage plus 10 more damage for each Colorless Energy in the Defending Pok\u00e9mon's Retreat Cost. Damage is calculated using the Defending Pok\u00e9mon's Retreat Cost after applying effects to the Retreat Cost.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=damage_per(count_retreat_cost(side="defender"), 10, base=40),
        ),
    ],
)