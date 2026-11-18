from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="f357b065-c716-5b73-9194-2f9cbbd1d2af",
    key="PL1",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ToxicroakG.Name",
    display_name="Toxicroak G",
    searchable_by=["Toxicroak G", "Basic", "SP", "ToxicroakG"],
    subtypes=["Basic", "SP"],
    collector_number=40,
    set_code="PL1",
    rarity=Rarities.Rare,
    hp=90,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=2,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=454,
    abilities=[
        Ability(
            title="Anticipation",
            game_text="Prevent all effects of attacks, excluding damage, done to Toxicroak G.",
            effect=unimplemented,
        ),
        Attack(
            title="Deep Poison",
            game_text="If the Defending Pok\u00e9mon is Poisoned, this attack does 20 damage plus 40 more damage.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=20,
            damage_operator="+",
            effect=unimplemented,
        ),
    ],
)