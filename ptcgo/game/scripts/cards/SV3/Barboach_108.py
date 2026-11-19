from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="6c8b1c20-aa95-57c3-b275-2e228abfd427",
    key="SV3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Barboach.Name",
    display_name="Barboach",
    searchable_by=["Barboach", "Basic", "Barboach"],
    subtypes=["Basic"],
    collector_number=108,
    set_code="SV3",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.GRASS,
    family_id=339,
    abilities=[
        Attack(
            title="Hide",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Mud-Slap",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
        ),
    ],
)