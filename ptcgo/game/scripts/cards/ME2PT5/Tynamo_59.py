from ptcgo.game.card_effects.support_common import heal_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="44f1db68-0701-53cb-9d7a-55abb4287e4b",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tynamo.Name",
    display_name="Tynamo",
    searchable_by=["Tynamo", "Basic", "Tynamo"],
    subtypes=["Basic"],
    collector_number=59,
    set_code="ME2PT5",
    rarity=Rarities.Common,
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