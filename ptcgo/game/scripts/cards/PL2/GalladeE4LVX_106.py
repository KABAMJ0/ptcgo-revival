from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import damage_counters_on, damage_per

card = PokemonCardDef(
    guid="14463a56-27d0-5480-b19c-9b39366a857e",
    key="PL2",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeE4LVX.Name",
    display_name="Gallade E4 LV.X",
    searchable_by=["Gallade E4 LV.X", "Level-Up", "SP", "GalladeE4LVX"],
    subtypes=["Level-Up", "SP"],
    collector_number=106,
    set_code="PL2",
    rarity=Rarities.RareHolo,
    hp=100,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    weakness_type=PokemonTypes.PSYCHIC,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.GalladeE4.Name",
    family_id=475,
    abilities=[
        Ability(
            title="Blade Storm",
            game_text="Once during your turn (before your attack), when you put Gallade E4 LV.X from your hand onto your Active Gallade E4, you may put 1 damage counter on each of your opponent's Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Aimed Cut",
            game_text="Does 40 damage plus 10 more damage for each damage counter on the Defending Pok\u00e9mon.",
            cost={PokemonTypes.PSYCHIC: 1, PokemonTypes.COLORLESS: 2},
            damage=40,
            damage_operator="+",
            effect=damage_per(damage_counters_on("defender"), 10, base=40),
        ),
    ],
)