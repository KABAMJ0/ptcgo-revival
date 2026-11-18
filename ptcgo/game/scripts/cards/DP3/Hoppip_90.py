from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="40065178-693f-5bda-b393-4024d6c8974a",
    key="DP3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Hoppip.Name",
    display_name="Hoppip",
    searchable_by=["Hoppip", "Basic", "Hoppip"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="DP3",
    rarity=Rarities.Common,
    hp=30,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=187,
    abilities=[
        Ability(
            title="Cottonweed",
            game_text="If Hoppip has any Grass Energy attached to it, the Retreat Cost for Hoppip is 0.",
            effect=unimplemented,
        ),
        Attack(
            title="Hover Heal",
            game_text="Remove all Special Conditions from Hoppip.",
            cost={PokemonTypes.GRASS: 1},
            damage=10,
            effect=unimplemented,
        ),
    ],
)