from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import flip_choice

card = PokemonCardDef(
    guid="acf04914-0757-5ed5-a44c-5d23417b0e8a",
    key="NEO4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Phanpy.Name",
    display_name="Phanpy",
    searchable_by=["Phanpy", "Basic", "Phanpy"],
    subtypes=["Basic"],
    collector_number=76,
    set_code="NEO4",
    rarity=Rarities.Common,
    hp=40,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.GRASS,
    resistance_type=PokemonTypes.LIGHTNING,
    family_id=231,
    abilities=[
        Attack(
            title="Crushing Step",
            game_text="Flip a coin. If heads, this attack does 10 damage plus 10 more damage; if tails, this attack does 10 damage.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=10,
            damage_operator="+",
            effect=flip_choice(heads=20, tails=10),
        ),
    ],
)