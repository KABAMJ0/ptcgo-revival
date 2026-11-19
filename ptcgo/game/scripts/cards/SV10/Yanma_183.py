from ptcgo.game.data_utils import Ability, Attack, PokemonCardDef, unimplemented
from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.attributes import PokemonStage, PokemonTypes, Rarities

card = PokemonCardDef(
    guid="6a7ba6cf-1e14-51d4-9f0a-43a865750194",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Yanma.Name",
    display_name="Yanma",
    searchable_by=["Yanma", "Basic", "Yanma"],
    subtypes=["Basic"],
    collector_number=183,
    set_code="SV10",
    rarity=Rarities.Rare,
    hp=70,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=193,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Razor Wing",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 1},
            damage=30,
        ),
    ],
)