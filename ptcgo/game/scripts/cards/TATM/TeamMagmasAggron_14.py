from ptcgo.game.data_utils import PokemonCardDef, Attack
from ptcgo.game.attributes import AttrID, PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import spread_damage
from ptcgo.game.card_effects.pokemon import is_fighting_energy
from ptcgo.game.session.passives import effective_max_hp


async def _rock_stomp(ctx):
    """Discard any number of Fighting Energy from your Pokemon; 40 damage
    each (the printed "40x" is a multiplier, so there is no base damage)."""
    pool = [energy for pokemon in ctx.my_pokemon_in_play()
            for energy in ctx.attached_energies(pokemon)
            if is_fighting_energy(energy)]
    picks = await ctx.choose_cards(
        pool, len(pool), minimum=0,
        prompt="Choose any number of Fighting Energy to discard") if pool else []
    if picks:
        await ctx.discard_cards(picks)
        await ctx.deal_damage(40 * len(picks))


async def _boulder_storm(ctx):
    """Printed damage to the Active, then 20 to each of the opponent's Benched
    Pokemon that has any damage counters on it."""
    def damaged(pokemon):
        return pokemon.get_attribute(AttrID.HP, 0) < effective_max_hp(
            ctx.board, pokemon)

    await spread_damage(20, side="opponent", also_base=True, pred=damaged)(ctx)


card = PokemonCardDef(
    guid="9cc137d2-308e-5ab1-9eec-0944c6a66bd8",
    key="TATM",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasAggron.Name",
    display_name="Team Magma's Aggron",
    searchable_by=["Team Magma's Aggron", "Stage 2", "TeamMagmasAggron"],
    subtypes=["Stage 2"],
    collector_number=14,
    set_code="TATM",
    rarity=Rarities.RareHolo,
    hp=140,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.TeamMagmasLairon.Name",
    family_id=304,
    abilities=[
        Attack(
            title="Rock Stomp",
            game_text="Discard as many Fighting Energy attached to your Pok\u00e9mon as you like. This attack does 40 damage times the amount of Fighting Energy you discarded.",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=40,
            damage_operator="x",
            effect=_rock_stomp,
        ),
        Attack(
            title="Boulder Storm",
            game_text="This attack does 20 damage to each of your opponent's Benched Pok\u00e9mon that has any damage counters on it. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 3, PokemonTypes.COLORLESS: 1},
            damage=120,
            effect=_boulder_storm,
        ),
    ],
)
