from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="45b2eedb-b132-508e-898d-e05805fade24",
    key="EX3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Golemex.Name",
    display_name="Golem ex",
    searchable_by=["Golem ex", "Stage 2", "ex", "Golemex"],
    subtypes=["Stage 2", "ex"],
    collector_number=91,
    set_code="EX3",
    rarity=Rarities.RareHolo,
    hp=160,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE2,
    retreat_cost=5,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Graveler.Name",
    family_id=74,
    abilities=[
        Attack(
            title="Magnitude",
            game_text="Does 10 damage to each Benched Pok\u00e9mon (both yours and your opponent's). (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=unimplemented,
        ),
        Attack(
            title="Double-edge",
            game_text="Golem ex does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 3},
            damage=120,
            effect=unimplemented,
        ),
    ],
)