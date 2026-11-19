from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per

card = PokemonCardDef(
    guid="7403c668-d3bb-5660-be02-0c4fc87517b3",
    key="SM11",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.MawileGX.Name",
    display_name="Mawile-GX",
    searchable_by=["Mawile-GX", "Basic", "GX", "MawileGX"],
    subtypes=["Basic", "GX"],
    collector_number=141,
    set_code="SM11",
    rarity=Rarities.RareHolo,
    hp=170,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.PSYCHIC,
    family_id=303,
    abilities=[
        Ability(
            title="Captivating Wink",
            game_text="When you play this Pok\u00e9mon from your hand onto your Bench during your turn, you may have your opponent reveal their hand and put any number of Basic Pok\u00e9mon you find there onto their Bench.",
            effect=unimplemented,
        ),
        Attack(
            title="Wily Bite",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), per=30, base=10),
        ),
        Attack(
            title="Big Eater-GX",
            game_text="Your opponent reveals their hand. Discard all Supporter cards you find there. (You can't use more than 1 GX attack in a game.)",
            cost={PokemonTypes.METAL: 1, PokemonTypes.COLORLESS: 1},
            effect=unimplemented,
        ),
    ],
)