from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="51308c9e-0c3d-533c-90c4-b4f35087a972",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Lucarioex.Name",
    display_name="Lucario ex",
    searchable_by=["Lucario ex", "Stage 1", "ex", "Lucarioex"],
    subtypes=["Stage 1", "ex"],
    collector_number=17,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=260,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Riolu.Name",
    family_id=448,
    abilities=[
        Attack(
            title="Low Sweep",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=60,
        ),
        Attack(
            title="Aura Sphere",
            game_text="This attack also does 50 damage to 1 of your opponent's Benched Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.FIGHTING: 2, PokemonTypes.COLORLESS: 1},
            damage=160,
            effect=unimplemented,
        ),
    ],
)