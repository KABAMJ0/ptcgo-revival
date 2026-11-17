from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="6b09a16f-57fb-574a-9d82-63d4e4e750ed",
    key="ME2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmot.Name",
    display_name="Pawmot",
    searchable_by=["Pawmot", "Stage 2", "Pawmot"],
    subtypes=["Stage 2"],
    collector_number=34,
    set_code="ME2",
    rarity=Rarities.Rare,
    hp=140,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Pawmo.Name",
    family_id=921,
    abilities=[
        Attack(
            title="Voltaic Fist",
            game_text="You may have this Pok\u00e9mon also do 60 damage to itself and make your opponent's Active Pok\u00e9mon Paralyzed.",
            cost={PokemonTypes.LIGHTNING: 2},
            damage=130,
            effect=unimplemented,
        ),
    ],
)