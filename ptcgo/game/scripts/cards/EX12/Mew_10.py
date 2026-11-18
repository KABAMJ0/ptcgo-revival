from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="cc7b0b85-53aa-539b-ae35-1763d2b02dcb",
    key="EX12",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Mew.Name",
    display_name="Mew",
    searchable_by=["Mew", "Basic", "Mew"],
    subtypes=["Basic"],
    collector_number=10,
    set_code="EX12",
    rarity=Rarities.RareHolo,
    hp=70,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    family_id=151,
    abilities=[
        Ability(
            title="Type Change",
            game_text="Once during your turn (before your attack), you may choose 1 of the Defending Pok\u00e9mon. Mew is the same type as that Pok\u00e9mon (all if that Pok\u00e9mon is more than 1 type) until the end of your turn. This power can't be used if Mew is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Link Blast",
            game_text="If Mew and the Defending Pok\u00e9mon have a different amount of Energy attached to them, this attack's base damage is 20 instead of 50.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 1},
            damage=50,
            effect=unimplemented,
        ),
    ],
)