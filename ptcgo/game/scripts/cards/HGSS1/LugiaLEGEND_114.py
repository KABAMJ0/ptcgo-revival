from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented, Triggers
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

from ptcgo.game.card_effects.trainers import is_energy_card


async def _ocean_grow_peek_top(ctx):
    top = ctx.deck_top(5)
    energies = [card for card in top if is_energy_card(card)]
    if energies:
        for card in energies:
            await ctx.attach_energy(card, ctx.source)
    rest = [card for card in top if card not in energies]
    if rest:
        await ctx.discard_cards(rest)


card = PokemonCardDef(
    guid="1b2a981e-2038-5ecc-ad4f-5ddabdd332a1",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.LugiaLEGEND.Name",
    display_name="Lugia LEGEND",
    searchable_by=["Lugia LEGEND", "LEGEND", "LugiaLEGEND"],
    subtypes=["LEGEND"],
    collector_number=114,
    set_code="HGSS1",
    rarity=Rarities.Common,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=249,
    abilities=[
        Ability(
            title="Ocean Grow",
            game_text="Once during your turn, when you put Lugia LEGEND into play, you may look at the top 5 cards of your deck and attach all Energy cards you find there to Lugia LEGEND. Discard the other cards.",
            trigger=Triggers.ON_PLAY,
            effect=_ocean_grow_peek_top,
        ),
        Attack(
            title="Elemental Blast",
            game_text="Discard a Fire Energy, Water Energy, and Lightning Energy attached to Lugia LEGEND.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.WATER: 1, PokemonTypes.LIGHTNING: 1},
            damage=200,
            effect=unimplemented,
        ),
    ],
)