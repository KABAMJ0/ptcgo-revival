from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import heal_attack

card = PokemonCardDef(
    guid="ec083637-9e6c-50fa-a223-e3ae090402ef",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Nacli.Name",
    display_name="Nacli",
    searchable_by=["Nacli", "Basic", "Nacli"],
    subtypes=["Basic"],
    collector_number=220,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.GRASS,
    family_id=932,
    abilities=[
        Attack(
            title="Salt Coating",
            game_text="Heal 20 damage from 1 of your Pok\u00e9mon.",
            cost={PokemonTypes.FIGHTING: 1},
            effect=heal_attack(20, target="choice"),
        ),
        Attack(
            title="Tackle",
            cost={PokemonTypes.FIGHTING: 2},
            damage=30,
        ),
    ],
)