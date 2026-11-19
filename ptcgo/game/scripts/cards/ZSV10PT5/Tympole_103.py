from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_with_attack, damage_per

card = PokemonCardDef(
    guid="1b78e977-22d7-59bb-b5a7-e6baecd94380",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tympole.Name",
    display_name="Tympole",
    searchable_by=["Tympole", "Basic", "Tympole"],
    subtypes=["Basic"],
    collector_number=103,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=60,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    family_id=535,
    abilities=[
        Attack(
            title="Round",
            game_text="This attack does 20 damage for each of your Pok\u00e9mon in play that has the Round attack.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            damage_operator="x",
            effect=damage_per(count_with_attack("Round"), 20),
        ),
    ],
)