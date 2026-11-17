from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="95f14d2b-46a4-5449-b402-f69cc23eb4b4",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanmegaex.Name",
    display_name="Yanmega ex",
    searchable_by=["Yanmega ex", "Stage 1", "ex", "Yanmegaex"],
    subtypes=["Stage 1", "ex"],
    collector_number=206,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=280,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE1,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    family_id=193,
    abilities=[
        Ability(
            title="Buzzing Boost",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may search your deck for up to 3 Basic Grass Energy cards and attach them to this Pok\u00e9mon. Then, shuffle your deck.",
            effect=unimplemented,
        ),
        Attack(
            title="Jet Cyclone",
            game_text="Move 3 Energy from this Pok\u00e9mon to 1 of your Benched Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 3, PokemonTypes.COLORLESS: 1},
            damage=210,
            effect=unimplemented,
        ),
    ],
)