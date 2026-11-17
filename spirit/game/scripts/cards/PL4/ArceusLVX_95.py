from spirit.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from spirit.game.attributes import PokemonTypes, PokemonStage, Rarities

card = PokemonCardDef(
    guid="50f9f171-dde9-538c-92f1-326b3845f2b7",
    key="PL4",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.ArceusLVX.Name",
    display_name="Arceus LV.X",
    searchable_by=["Arceus LV.X", "Level-Up", "ArceusLVX"],
    subtypes=["Level-Up"],
    collector_number=95,
    set_code="PL4",
    rarity=Rarities.RareHolo,
    hp=120,
    elements=[PokemonTypes.COLORLESS],
    stage=PokemonStage.BASIC,
    retreat_cost=1,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Arceus.Name",
    family_id=493,
    abilities=[
        Ability(
            title="Multitype",
            game_text="Arceus LV.X's type is the same as its previous Level.",
            effect=unimplemented,
        ),
        Attack(
            title="Meteor Blast",
            game_text="Flip a coin. If tails, this attack's base damage is 50 instead of 100.",
            cost={PokemonTypes.GRASS: 1, PokemonTypes.FIRE: 1, PokemonTypes.COLORLESS: 1},
            damage=100,
            effect=unimplemented,
        ),
    ],
)