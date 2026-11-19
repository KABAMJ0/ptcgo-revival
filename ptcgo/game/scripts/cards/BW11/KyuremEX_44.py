from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import mill_attack
card = PokemonCardDef(
    guid="f86a9c59-9c3b-502f-9e2a-063c38ce51f7",
    key="BW11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.KyuremEX.Name",
    display_name="Kyurem-EX",
    searchable_by=["Kyurem-EX", "Basic", "EX", "KyuremEX"],
    subtypes=["Basic", "EX"],
    collector_number=44,
    set_code="BW11",
    rarity=Rarities.RareHolo,
    hp=180,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Frozen Wings",
            game_text="Discard a Special Energy attached to the Defending Pok\u00e9mon.",
            cost={PokemonTypes.WATER: 1, PokemonTypes.COLORLESS: 2},
            damage=60,
            effect=mill_attack(2, opponent=False),
        ),
        Attack(
            title="Hail Blizzard",
            game_text="This Pok\u00e9mon can't use Hail Blizzard during your next turn.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=120,
            effect=unimplemented,
        ),
    ],
)