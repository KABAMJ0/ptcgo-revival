from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="264a936a-889c-5840-aa30-b9e4f085d508",
    key="PL3",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.StaraptorFBLVX.Name",
    display_name="Staraptor FB LV.X",
    searchable_by=["Staraptor FB LV.X", "Level-Up", "SP", "StaraptorFBLVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=147,
    set_code="PL3",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=0,
    weakness_type=PokemonTypes.LIGHTNING,
    resistance_type=PokemonTypes.FIGHTING,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.StaraptorFB.Name",
    family_id=398,
    abilities=[
        Ability(
            title="Fast Call",
            game_text="Once during your turn (before your attack), you may search your deck for a Supporter card, show it to your opponent, and put it into your hand. Shuffle your deck afterward. This power can't be used if Staraptor FB is affected by a Special Condition.",
            effect=unimplemented,
        ),
        Attack(
            title="Defog",
            game_text="Before doing damage, you may discard any Stadium card in play. If you do, this attack's base damage is 70 instead of 40.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=40,
            effect=unimplemented,
        ),
    ],
)