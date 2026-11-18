from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import (
    bonus_if,
    discard_opponent_energy_attack,
    stadium_in_play_cond,
)

card = PokemonCardDef(
    guid="7097af38-dc1e-50ab-b6c7-7b4f58fe2da2",
    key="SM12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.BlackKyurem.Name",
    display_name="Black Kyurem",
    searchable_by=["Black Kyurem", "Basic", "BlackKyurem"],
    subtypes=["Basic"],
    collector_number=61,
    set_code="SM12",
    rarity=Rarities.RareHolo,
    hp=130,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.BASIC,
    retreat_cost=3,
    weakness_type=PokemonTypes.METAL,
    family_id=646,
    abilities=[
        Attack(
            title="Frozen Wings",
            game_text="Discard a Special Energy from your opponent's Active Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=30,
            effect=discard_opponent_energy_attack(special_only=True),
        ),
        Attack(
            title="Dazzling Blizzard",
            game_text="If you have any Stadium card in play, this attack does 100 more damage.",
            cost={PokemonTypes.WATER: 2, PokemonTypes.COLORLESS: 2},
            damage=100,
            damage_operator="+",
            effect=bonus_if(stadium_in_play_cond, 100),
        ),
    ],
)