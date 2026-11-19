from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import discard_for_bonus
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_bench, damage_per

card = PokemonCardDef(
    guid="939acca4-2383-5459-9386-f66eb6c6963b",
    key="SWSH10TG",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IceRiderCalyrexVMAX.Name",
    display_name="Ice Rider Calyrex VMAX",
    searchable_by=["Ice Rider Calyrex VMAX", "VMAX", "IceRiderCalyrexVMAX"],
    subtypes=["VMAX"],
    collector_number=15,
    set_code="SWSH10TG",
    rarity=Rarities.RareHoloVMAX,
    hp=320,
    elements=[PokemonTypes.WATER],
    stage=PokemonStage.VMAX,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.IceRiderCalyrexV.Name",
    family_id=898,
    abilities=[
        Attack(
            title="Ride of the High King",
            game_text="This attack does 30 more damage for each of your opponent's Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=10,
            damage_operator="+",
            effect=damage_per(count_bench("opponent"), per=30, base=10),
        ),
        Attack(
            title="Max Lance",
            game_text="You may discard up to 2 Energy from this Pok\u00e9mon. If you do, this attack does 120 more damage for each card you discarded in this way.",
            cost={PokemonTypes.WATER: 2},
            damage=10,
            damage_operator="+",
            effect=discard_for_bonus(source="self-energy", max_count=2, per=120),
        ),
    ],
)