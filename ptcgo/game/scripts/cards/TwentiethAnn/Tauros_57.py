from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import recoil_attack

card = PokemonCardDef(
    guid="ebe48d4d-02ef-59e4-b0fe-0e68ef2066a8",
    key="TwentiethAnn",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Tauros.Name",
    display_name="Tauros",
    searchable_by=["Tauros", "Basic", "Tauros"],
    subtypes=["Basic"],
    collector_number=57,
    set_code="TwentiethAnn",
    rarity=Rarities.Rare,
    hp=110,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=128,
    abilities=[
        Attack(
            title="Take Down",
            game_text="This Pok\u00e9mon does 10 damage to itself.",
            cost={PokemonTypes.COLORLESS: 1},
            damage=30,
            effect=recoil_attack(10),
        ),
        Attack(
            title="Seething Anger",
            game_text="Flip a coin for each damage counter on this Pok\u00e9mon. This attack does 30 damage times the number of heads.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=30,
            damage_operator="x",
            effect=unimplemented,
        ),
    ],
)