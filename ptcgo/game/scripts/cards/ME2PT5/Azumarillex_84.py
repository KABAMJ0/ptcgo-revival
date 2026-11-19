from ptcgo.game.card_effects.attacks_common import count_energy
from ptcgo.game.card_effects.attacks_common import damage_per
from ptcgo.game.data_utils import PokemonCardDef, Attack, Ability, unimplemented
from ptcgo.game.attributes import PokemonTypes, PokemonStage, Rarities
from ptcgo.game.card_effects.attacks_common import count_energy, damage_per

card = PokemonCardDef(
    guid="922c768d-2c76-5d86-a1b2-08e2d77214d5",
    key="ME2PT5",
    name="com.direwolfdigital.cake.data.archetypes.pokemon.Azumarillex.Name",
    display_name="Azumarill ex",
    searchable_by=["Azumarill ex", "Stage 1", "ex", "Azumarillex"],
    subtypes=["Stage 1", "ex"],
    collector_number=84,
    set_code="ME2PT5",
    rarity=Rarities.Rare,
    hp=270,
    elements=[PokemonTypes.PSYCHIC],
    stage=PokemonStage.STAGE1,
    retreat_cost=2,
    weakness_type=PokemonTypes.METAL,
    evolves_from="com.direwolfdigital.cake.data.archetypes.pokemon.Marill.Name",
    family_id=183,
    abilities=[
        Ability(
            title="Bubble Gathering",
            game_text="As often as you like during your turn, you may use this Ability. Move an Energy from 1 of your other Pok\u00e9mon to this Pok\u00e9mon.",
            effect=unimplemented,
        ),
        Attack(
            title="Energized Balloon",
            game_text="This attack does 40 more damage for each Psychic Energy attached to this Pok\u00e9mon.",
            cost={PokemonTypes.COLORLESS: 3},
            damage=60,
            damage_operator="+",
            effect=damage_per(count_energy("self", PokemonTypes.PSYCHIC), per=40, base=60),
        ),
    ],
)