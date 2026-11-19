from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.passives_common import flip_protection

card = PokemonCardDef(
    guid="4fc49611-cfc4-5b65-a78b-5f3521041305",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Sudowoodo.Name",
    display_name="Sudowoodo",
    searchable_by=["Sudowoodo", "Basic", "Sudowoodo"],
    subtypes=["Basic"],
    collector_number=109,
    set_code="SV2",
    rarity=Rarities.Uncommon,
    hp=110,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    family_id=185,
    abilities=[
        Attack(
            title="Hit and Hide",
            game_text="Flip a coin. If heads, during your opponent's next turn, prevent all damage from and effects of attacks done to this Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=20,
            effect=flip_protection(prevent=True, effects_too=True),
        ),
        Attack(
            title="Elbow Strike",
            cost={PokemonTypes.FIGHTING: 1, PokemonTypes.COLORLESS: 2},
            damage=90,
        ),
    ],
)