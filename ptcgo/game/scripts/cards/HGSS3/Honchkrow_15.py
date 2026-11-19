from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.support_common import gust_attack

card = PokemonCardDef(
    guid="de62af38-cb7c-5eca-b6d5-6724d9ed60f0",
    key="HGSS3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Honchkrow.Name",
    display_name="Honchkrow",
    searchable_by=["Honchkrow", "Stage 1", "Honchkrow"],
    subtypes=["Stage 1"],
    collector_number=15,
    set_code="HGSS3",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.DARKNESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Murkrow.Name",
    family_id=198,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Blindside",
            game_text="Choose 1 of your opponent's Pok\u00e9mon that has any damage counters on it. This attack does 50 damage to that Pok\u00e9mon. (Don't apply Weakness and Resistance for Benched Pok\u00e9mon.)",
            cost={PokemonTypes.DARKNESS: 2},
            effect=unimplemented,
        ),
    ],
)