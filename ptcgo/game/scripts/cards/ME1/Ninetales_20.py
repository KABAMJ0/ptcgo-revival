from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="a6b3963b-1dae-5ee5-b522-ffaa14a5c2c0",
    key="ME1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Ninetales.Name",
    display_name="Ninetales",
    searchable_by=["Ninetales", "Stage 1", "Ninetales"],
    subtypes=["Stage 1"],
    collector_number=20,
    set_code="ME1",
    rarity=Rarities.Uncommon,
    hp=120,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Vulpix.Name",
    family_id=37,
    abilities=[
        Attack(
            title="Supernatural Shapeshifter",
            game_text="Discard the top card of your deck, and if that card is a Supporter card, use the effect of that card as the effect of this attack.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
        Attack(
            title="Combustion",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
    ],
)