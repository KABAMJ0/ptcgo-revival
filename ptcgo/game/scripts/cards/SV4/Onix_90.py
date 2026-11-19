from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="e5708535-1837-58da-9278-656e6a042aa6",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Onix.Name",
    display_name="Onix",
    searchable_by=["Onix", "Basic", "Onix"],
    subtypes=["Basic"],
    collector_number=90,
    set_code="SV4",
    rarity=Rarities.Common,
    hp=120,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.GRASS,
    family_id=95,
    abilities=[
        Attack(
            title="Hard Headbutt",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Land Crush",
            cost={PokemonTypes.COLORLESS: 3},
            damage=80,
        ),
    ],
)