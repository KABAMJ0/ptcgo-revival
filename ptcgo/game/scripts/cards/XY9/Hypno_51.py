from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="326f178e-93e8-5403-bcd0-778cc7c1e51e",
    key="XY9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hypno.Name",
    display_name="Hypno",
    searchable_by=["Hypno", "Stage 1", "Hypno"],
    subtypes=["Stage 1"],
    collector_number=51,
    set_code="XY9",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Drowzee.Name",
    family_id=96,
    abilities=[
        Ability(
            title="Goodnight, Babies",
            game_text="Once during your turn (before your attack), you may leave both Active Pok\u00e9mon Asleep.",
            effect=unimplemented,
        ),
        Attack(
            title="Zen Headbutt",
            cost={PokemonTypes.PSYCHIC: 2},
            damage=50,
        ),
    ],
)