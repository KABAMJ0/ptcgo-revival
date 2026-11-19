from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="de4db5a5-c283-52a4-ae60-ff45a37b7375",
    key="SV4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Armarougeex.Name",
    display_name="Armarouge ex",
    searchable_by=["Armarouge ex", "Stage 1", "ex", "Armarougeex"],
    subtypes=["Stage 1", "ex"],
    collector_number=218,
    set_code="SV4",
    rarity=Rarities.Rare,
    hp=260,
    elements=[PokemonTypes.FIRE],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.WATER,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Charcadet.Name",
    family_id=935,
    abilities=[
        Ability(
            title="Crimson Armor",
            game_text="If this Pok\u00e9mon has full HP, it takes 80 less damage from attacks from your opponent's Pok\u00e9mon (after applying Weakness and Resistance).",
            effect=damage_per(count_energy("self", "fire"), 40),
        ),
        Attack(
            title="Scorching Bazooka",
            game_text="This attack does 40 more damage for each Fire Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.FIRE), per=40, base=40),
        ),
    ],
)