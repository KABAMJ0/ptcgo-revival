from ptcgo.game.data_utils import (
    PokemonCardDef, Attack, Ability, Activations, unimplemented,
)
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities


async def propagation(ctx) -> None:
    """From the discard pile: put this Pokemon into your hand."""
    if not await ctx.ask_yes_no("Put this Pokémon into your hand?"):
        return
    await ctx.put_in_hand([ctx.source])


card = PokemonCardDef(
    guid="a0c73251-03d7-5750-9b82-f806ac3a4fa9",
    key="BW10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Exeggcute.Name",
    display_name="Exeggcute",
    searchable_by=["Exeggcute", "Basic", "Exeggcute"],
    subtypes=["Basic"],
    collector_number=102,
    set_code="BW10",
    rarity=Rarities.RareSecret,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    family_id=102,
    abilities=[
        Ability(
            title="Propagation",
            game_text="Once during your turn (before your attack), if this Pok\u00e9mon is in your discard pile, you may put this Pok\u00e9mon into your hand.",
            activation=Activations.ONCE_PER_TURN,
            usable_from="discard",
            effect=propagation,
        ),
        Attack(
            title="Seed Bomb",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)