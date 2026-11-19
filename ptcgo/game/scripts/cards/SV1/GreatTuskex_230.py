from ptcgo.game.card_effects.attacks_common import recoil_attack, discard_stadium_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="8e376ed6-eb0e-524b-bc85-319ee97249c5",
    key="SV1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GreatTuskex.Name",
    display_name="Great Tusk ex",
    searchable_by=["Great Tusk ex", "Basic", "ex", "GreatTuskex"],
    subtypes=["Basic", "ex"],
    collector_number=230,
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