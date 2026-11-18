from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="e67e2b67-9c07-5ff0-9ffe-b6e22deab010",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Volcarona.Name",
    display_name="Volcarona",
    searchable_by=["Volcarona", "Stage 1", "Volcarona"],
    subtypes=["Stage 1"],
    collector_number=29,
    set_code="SV9",
    rarity=Rarities.Uncommon,
    hp=140,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Larvesta.Name",
    family_id=636,
    abilities=[
        Attack(
            title="Smoldering Scales",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=80,
        ),
    ],
)