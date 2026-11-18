from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="05d35705-8baf-58c8-98af-05d508deae8d",
    key="SV9",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Shelmet.Name",
    display_name="Shelmet",
    searchable_by=["Shelmet", "Basic", "Shelmet"],
    subtypes=["Basic"],
    collector_number=12,
    set_code="SV9",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    family_id=616,
    abilities=[
        Attack(
            title="Shell Smack",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage done to this Pok\u00e9mon by attacks.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_protection(prevent=True),
        ),
    ],
)