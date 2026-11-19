from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import lock_self_attack

card = PokemonCardDef(
    guid="fdf03630-c3f6-5168-a28d-b2d95a50c6f1",
    key="SVP",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronValiantex.Name",
    display_name="Iron Valiant ex",
    searchable_by=["Iron Valiant ex", "Basic", "ex", "Future", "IronValiantex"],
    subtypes=["Basic", "ex", "Future"],
    collector_number=68,
    set_code="SVP",
    rarity=Rarities.RarePromo,
    hp=220,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    family_id=1006,
    abilities=[
        Ability(
            title="Tachyon Bits",
            game_text="Once during your turn, when this Pok\u00e9mon moves from your Bench to the Active Spot, you may put 2 damage counters on 1 of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Laser Blade",
            game_text="During your next turn, this Pok\u00e9mon can't attack.",
            cost={PokemonTypes.PSYCHIC: 2, PokemonTypes.COLORLESS: 1},
            damage=200,
            effect=lock_self_attack(),
        ),
    ],
)