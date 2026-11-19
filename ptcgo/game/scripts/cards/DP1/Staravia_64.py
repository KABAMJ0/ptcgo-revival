from ptcgo.game.card_effects.support_common import gust_attack
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import no_retreat_attack

card = PokemonCardDef(
    guid="dcb87214-e2e9-5b13-bf25-792c26d1557d",
    key="DP1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Staravia.Name",
    display_name="Staravia",
    searchable_by=["Staravia", "Stage 1", "Staravia"],
    subtypes=["Stage 1"],
    collector_number=64,
    set_code="DP1",
    rarity=Rarities.Uncommon,
    hp=70,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.STAGE1,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Starly.Name",
    family_id=396,
    abilities=[
        Attack(
            title="Whirlwind",
            game_text="Your opponent switches the Defending Pok\u00e9mon with 1 of his or her Benched Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=gust_attack(opponent_chooses=True),
        ),
        Attack(
            title="Clutch",
            game_text="The Defending Pok\u00e9mon can't retreat during your opponent's next turn.",
            cost={PokemonTypes.COLORLESS: 2},
            damage=20,
            effect=no_retreat_attack(),
        ),
    ],
)