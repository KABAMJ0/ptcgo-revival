from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="78abdd5d-cb94-5d55-8688-ffdaae4595b6",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.NsReshiram.Name",
    display_name="N's Reshiram",
    searchable_by=["N's Reshiram", "Basic", "NsReshiram"],
    subtypes=["Basic"],
    collector_number=154,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=130,
    elements=[PokemonTypes.DRAGON],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    family_id=643,
    abilities=[
        Attack(
            title="Powerful Rage",
            game_text="This attack does 20 damage for each damage counter on this Pok\u00e9mon.",
            cost={PokemonTypes.FIRE: 1, PokemonTypes.LIGHTNING: 1},
            damage=20,
            damage_operator="x",
            effect=damage_per(damage_counters_on("self"), 20),
        ),
        Attack(
            title="Virtuous Flame",
            cost={PokemonTypes.FIRE: 2, PokemonTypes.LIGHTNING: 1, PokemonTypes.COLORLESS: 1},
            damage=170,
        ),
    ],
)