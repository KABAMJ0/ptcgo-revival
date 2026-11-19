from ptcgo.game.card_effects.attacks_common import mill_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="2d4ebb16-c454-5d9d-ab8e-257324250c58",
    key="SV2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ChiYuex.Name",
    display_name="Chi-Yu ex",
    searchable_by=["Chi-Yu ex", "Basic", "ex", "ChiYuex"],
    subtypes=["Basic", "ex"],
    collector_number=40,
    set_code="SV2",
    rarity=Rarities.Rare,
    hp=190,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.WATER,
    family_id=1004,
    abilities=[
        Attack(
            title="Jealously Singe",
            game_text="Discard the top 2 cards of your opponent's deck.",
            cost={PokemonTypes.FIRE: 1},
            effect=mill_attack(2, opponent=True),
        ),
        Attack(
            title="Flame Surge",
            game_text="Choose up to 3 of your Benched Pok\u00e9mon. For each of those Pok\u00e9mon, search your deck for a Basic Fire Energy card and attach it to that Pok\u00e9mon. Then, shuffle your deck.",
            cost={PokemonTypes.FIRE: 2},
            damage=100,
            effect=unimplemented,
        ),
    ],
)