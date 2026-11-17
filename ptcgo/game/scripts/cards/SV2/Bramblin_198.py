from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="fb84af48-4fd2-53ce-a0a7-6494eb662f45",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Bramblin.Name",
    display_name="Bramblin",
    searchable_by=["Bramblin", "Basic", "Bramblin"],
    subtypes=["Basic"],
    collector_number=198,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=50,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    family_id=946,
    abilities=[
        Attack(
            title="Blot",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)