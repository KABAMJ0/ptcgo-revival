from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import search_to_hand
from ptcgo.game.card_effects.passives_common import team_damage_boost_passive



card = PokemonCardDef(
    guid="e9a159fb-7415-544f-bc50-5f6e1b0cff04",
    key="ZSV10PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Serperiorex.Name",
    display_name="Serperior ex",
    searchable_by=["Serperior ex", "Stage 2", "ex", "Serperiorex"],
    subtypes=["Stage 2", "ex"],
    collector_number=164,
    set_code="ZSV10PT5",
    rarity=Rarities.Rare,
    hp=320,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Servine.Name",
    family_id=495,
    abilities=[
        Ability(
            title="Regal Cheer",
            game_text="Attacks used by your Pok\u00e9mon do 20 more damage to your opponent's Active Pok\u00e9mon (before applying Weakness and Resistance).",
            passive=team_damage_boost_passive(20),
        ),
        Attack(
            title="Command the Grass",
            game_text="You may search your deck for up to 3 cards and put them into your hand. Then, shuffle your deck.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.COLORLESS: 3},
            damage=150,
            effect=search_to_hand(None, count=3, reveal=False),
        ),
    ],
)