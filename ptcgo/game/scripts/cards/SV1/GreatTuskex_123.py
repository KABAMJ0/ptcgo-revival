from ptcgo.game.card_effects.attacks_common import recoil_attack, discard_stadium_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import discard_stadium_attack


card = PokemonCardDef(
    guid="4c7877a7-6b14-5f80-9034-81a059282214",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTuskex.Name",
    display_name="Great Tusk ex",
    searchable_by=["Great Tusk ex", "Basic", "ex", "GreatTuskex"],
    subtypes=["Basic", "ex"],
    collector_number=123,
    set_code="SV1",
    rarity=Rarities.Rare,
    hp=250,
    elements=[PokemonTypes.FIGHTING],
    stage=PokemonStage.BASIC,
    retreat_cost=4,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=984,
    abilities=[
        Attack(
            title="Bedrock Breaker",
            game_text="Discard a Stadium in play.",
            cost={PokemonTypes.FIGHTING: 1},
            damage=40,
            effect=discard_stadium_attack(),
        ),
        Attack(
            title="Gigantic Tusks",
            game_text="This Pok\u00e9mon also does 50 damage to itself.",
            cost={PokemonTypes.FIGHTING: 3},
            damage=250,
            effect=recoil_attack(50),
        ),
    ],
)