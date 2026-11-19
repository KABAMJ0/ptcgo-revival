from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="6e604e88-83f8-558e-a28f-693ba911c412",
    key="SV4PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Cyclizar.Name",
    display_name="Cyclizar",
    searchable_by=["Cyclizar", "Basic", "Cyclizar"],
    subtypes=["Basic"],
    collector_number=195,
    set_code="SV4PT5",
    rarity=Rarities.Rare,
    hp=120,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    family_id=967,
    abilities=[
        Attack(
            title="Acceleration Drive",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.DARKNESS: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
    ],
)