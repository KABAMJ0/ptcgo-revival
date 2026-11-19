from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="3a921c30-3587-5dcf-8fc0-521572a4d08b",
    key="SV10",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Squawkabilly.Name",
    display_name="Squawkabilly",
    searchable_by=["Squawkabilly", "Basic", "Squawkabilly"],
    subtypes=["Basic"],
    collector_number=160,
    set_code="SV10",
    rarity=Rarities.Common,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=931,
    abilities=[
        Attack(
            title="Push Down",
            game_text="You may switch out your opponent's Active Pok\u00e9mon to the Bench. (Your opponent chooses the new Active Pok\u00e9mon.)",
            cost={PokemonTypes.COLORLESS: 1},
            damage=20,
            effect=gust_attack(opponent_chooses=True, damage_before=0),
        ),
    ],
)