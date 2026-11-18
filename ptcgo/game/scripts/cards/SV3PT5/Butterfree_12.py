from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="7af584a1-730f-5023-9563-4d0312cfef87",
    key="SV3PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Butterfree.Name",
    display_name="Butterfree",
    searchable_by=["Butterfree", "Stage 2", "Butterfree"],
    subtypes=["Stage 2"],
    collector_number=12,
    set_code="SV3PT5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.GRASS],
    stage=PokemonStage.STAGE2,
    retreat_cost=1,
    weakness_type=PokemonTypes.FIRE,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metapod.Name",
    family_id=10,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.)",
            cost={PokemonTypes.GRASS: 1},
            damage=60,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Bye-Bye Flight",
            game_text="Choose 1 of your opponent's Benched Pok\u00e9mon. Shuffle that Pok\u00e9mon and all attached cards into their deck, and then shuffle this Pok\u00e9mon and all attached cards into your deck. If your opponent has no Benched Pok\u00e9mon, this attack does nothing.",
            cost={PokemonTypes.COLORLESS: 2},
            effect=unimplemented,
        ),
    ],
)