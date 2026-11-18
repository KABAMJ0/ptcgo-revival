from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f9d401d2-f911-56f5-b3b1-98f062290f0c",
    key="SV5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.IronJugulis.Name",
    display_name="Iron Jugulis",
    searchable_by=["Iron Jugulis", "Basic", "Future", "IronJugulis"],
    subtypes=["Basic", "Future"],
    collector_number=139,
    set_code="SV5",
    rarity=Rarities.Uncommon,
    hp=130,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    family_id=993,
    abilities=[
        Ability(
            title="Automated Combat",
            game_text="If this Pok\u00e9mon is in the Active Spot and is damaged by an attack from your opponent's Pok\u00e9mon (even if this Pok\u00e9mon is Knocked Out), put 3 damage counters on the Attacking Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Blasting Wind",
            cost={PokemonTypes.COLORLESS: 3},
            damage=110,
        ),
    ],
)