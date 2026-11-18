from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="4a04897e-935c-5df0-9e52-b00cbc0f93a9",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo", "Basic", "Tynamo"],
    subtypes=["Basic"],
    collector_number=113,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=40,
    elements=[PokemonTypes.LIGHTNING],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=602,
    abilities=[
        Attack(
            title="Hold Still",
            game_text="Heal 10 damage from this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 1},
            effect=heal_attack(10),
        ),
    ],
)