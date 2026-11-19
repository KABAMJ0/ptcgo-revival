from ptcgo.game.card_effects.attacks_common import flip_bonus
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="5195c3a2-ae4c-57c4-9cb5-3af770586221",
    key="SM4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Miltank.Name",
    display_name="Miltank",
    searchable_by=["Miltank", "Basic", "Miltank"],
    subtypes=["Basic"],
    collector_number=78,
    set_code="SM4",
    rarity=Rarities.Uncommon,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.FIGHTING,
    family_id=241,
    abilities=[
        Ability(
            title="Moomoo Malt",
            game_text="As long as this Pok\u00e9mon is your Active Pok\u00e9mon, whenever you attach an Energy card from your hand to 1 of your Pok\u00e9mon, heal 90 damage from that Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Sitdown Splash",
            game_text="Flip a coin. If heads, this attack does 30 more damage.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=flip_bonus(30),
        ),
    ],
)