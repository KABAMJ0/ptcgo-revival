from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3387db38-6d91-536d-9d1b-edac25c8d752",
    key="SV8",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Zarude.Name",
    display_name="Zarude",
    searchable_by=["Zarude", "Basic", "Zarude"],
    subtypes=["Basic"],
    collector_number=11,
    set_code="SV8",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=893,
    abilities=[
        Attack(
            title="Leaf Drain",
            game_text="Heal 20 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=20,
            effect=unimplemented,
        ),
        Attack(
            title="Jungle Whip",
            game_text="You may put all Energy attached to this Pok\u00e9mon into your hand to have this attack do 80 more damage.",
            cost={PokemonTypes.GRASS: 2, PokemonTypes.COLORLESS: 1},
            damage=80,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)