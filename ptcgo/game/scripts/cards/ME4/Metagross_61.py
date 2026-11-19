from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="62696373-03a8-5971-a5c0-3200a5b9a750",
    key="ME4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Metagross.Name",
    display_name="Metagross",
    searchable_by=["Metagross", "Stage 2", "Metagross"],
    subtypes=["Stage 2"],
    collector_number=61,
    set_code="ME4",
    rarity=Rarities.Uncommon,
    hp=180,
    elements=[PokemonTypes.METAL],
    stage=PokemonStage.STAGE2,
    retreat_cost=3,
    weakness_type=PokemonTypes.FIRE,
    resistance_type=PokemonTypes.GRASS,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Metang.Name",
    family_id=374,
    abilities=[
        Attack(
            title="Bounce Back",
            game_text="Switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.)",
            cost={PokemonTypes.METAL: 1},
            damage=60,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Metallic Hammer",
            game_text="You may discard 3 Metal Energy from this Pok\u00e9mon and have this attack do 150 more damage.",
            cost={PokemonTypes.METAL: 3, PokemonTypes.COLORLESS: 1},
            damage=150,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)