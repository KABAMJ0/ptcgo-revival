from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="d36510d8-0f42-5471-a5cc-c3ad3f277b77",
    key="HGSS1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Meganium.Name",
    display_name="Meganium",
    searchable_by=["Meganium", "Stage 2", "Prime", "Meganium"],
    subtypes=["Stage 2", "Prime"],
    collector_number=109,
    set_code="HGSS1",
    rarity=Rarities.Rare,
    hp=150,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Bayleef.Name",
    family_id=152,
    abilities=[
        Ability(
            title="Leaf Trans",
            game_text="As often as you like during your turn (before your attack), you may move a Grass Energy attached to 1 of your Pok\u00e9mon to another of your Pok\u00e9mon. This power can't be used if Meganium is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Solarbeam",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 2},
            damage=80,
        ),
    ],
)