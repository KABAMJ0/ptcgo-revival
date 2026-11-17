from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="538ab16c-a36e-5207-9337-2a936c890a0d",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Gastrodon.Name",
    display_name="Gastrodon",
    searchable_by=["Gastrodon", "Stage 1", "Gastrodon"],
    subtypes=["Stage 1"],
    collector_number=107,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Shellos.Name",
    family_id=422,
    abilities=[
        Ability(
            title="Sticky Bind",
            game_text="As long as this Pok\u00e9mon is on your Bench, Benched Stage 2 Pok\u00e9mon (both yours and your opponent's) have no Abilities.",
            effect=unimplemented,
        ),
        Attack(
            title="Mud Shot",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)