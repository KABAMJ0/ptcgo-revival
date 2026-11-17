from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4d370f86-d7b6-5146-8b76-deba9ce148b6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IonosKilowattrel.Name",
    display_name="Iono's Kilowattrel",
    searchable_by=["Iono's Kilowattrel", "Stage 1", "IonosKilowattrel"],
    subtypes=["Stage 1"],
    collector_number=72,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IonosWattrel.Name",
    family_id=940,
    abilities=[
        Ability(
            title="Flashing Draw",
            game_text="You must discard a Basic Lightning Energy from this Pok\u00e9mon in order to use this Ability. Once during your turn, you may draw cards until you have 6 cards in your hand.",
            effect=unimplemented,
        ),
        Attack(
            title="Mach Bolt",
            cost={PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 2},
            damage=70,
        ),
    ],
)